#![allow(dead_code)]
use std::cmp;


// Solve the rectangle tiling problem using a greedy algorithm.
struct GreedySolver {
    total_length : i32,
    total_width : i32,
    length : i32,
    width : i32,
}

impl GreedySolver {
    fn new(length: i32, width: i32) -> GreedySolver {
        GreedySolver {
            total_length: length,
            total_width: width,
            length: cmp::max(length, width),
            width:  cmp::min(length, width),
        }
    }
}

impl Iterator for GreedySolver {
    type Item = (i32, i32);

    #[inline]
    fn next(&mut self) -> Option<Self::Item> {
        let next_length = cmp::min(self.length, self.width);
        let side1 = self.length - next_length;
        let side2 = self.width - next_length;
        // At least one of the sides is nonzero since we subtract the minimum
        // of two sides above.
        let next_width = cmp::max(side1, side2);

        self.length = next_length;
        self.width  = next_width;

        if next_length > 0 {
            Some((next_length, next_width))
        } else {
            None
        }
    }
}

fn sq_in_rect(length: i32, width: i32) -> Option<Vec<i32>> {
    if length == width {
        // This seems like a silly constraint to impose on
        // tiling a rectangle with squares; squares can
        // appear in the tiling subproblems.
        None
    } else {
        let solver = GreedySolver::new(length, width);
        let sides = solver.map(|(side1, _)| { side1 }).collect::<Vec<_>>();
    
        Some(sides)
    }
}

#[cfg(test)]
mod tests {
    fn testing(length: i32, width: i32, expected: Option<Vec<i32>>) -> () {
        assert_eq!(super::sq_in_rect(length, width), expected);
    }

    #[test]
    fn tests_sq_in_rect() {
        testing(5, 3,  Some(vec![3, 2, 1, 1]));
        testing(3, 5,  Some(vec![3, 2, 1, 1]));
        testing(5, 5,  None);
        testing(5, 1,  Some(vec![1, 1, 1, 1, 1]));
        testing(1, 7,  Some(vec![1, 1, 1, 1, 1, 1, 1]));
        testing(15, 6, Some(vec![6, 6, 3, 3]));
    }
}

#![allow(dead_code)]
use std::cmp;


#[inline]
fn step(length: i32, width: i32) -> (i32, i32) {
    let longer_side  = cmp::min(length, width);
    let new_length   = length - longer_side;
    let new_width    = width - longer_side;
    // At least one of the sides is nonzero since we subtract the minimum
    // of two sides above.
    let shorter_side = cmp::max(new_length, new_width);

    (longer_side, shorter_side)
}

// Solve the rectangle tiling problem using a greedy algorithm.
fn sq_in_rect(length: i32, width: i32) -> Option<Vec<i32>> {
    if length == width {
        return None;
    }
    
    let mut sides = vec![];
    let mut rect = (cmp::max(length, width), cmp::min(length, width));
    loop {
        rect = step(rect.0, rect.1);
        let side = rect.0;

        if side <= 0 {
            break;
        }

        sides.push(side);
    }
    
    Some(sides)
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

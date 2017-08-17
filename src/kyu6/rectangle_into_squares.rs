#![allow(dead_code)]


fn min(x: i32, y: i32) -> i32 {
    if x > y { y } else { x }
}

fn max(x: i32, y: i32) -> i32 {
    if x > y { x } else { y }
}

fn step(length: i32, width: i32) -> (i32, i32) {
    let side1      = min(length, width);
    let new_length = length - side1;
    let new_width  = width - side1;
    // At least one of the sides is nonzero since we subtract the minimum
    // of two sides above.
    let side2      = max(new_length, new_width);

    (side1, side2)
}

fn sq_in_rect(length: i32, width: i32) -> Option<Vec<i32>> {
    if (length == width) && (length != 0) && (width != 0) {
        return None;
    }
    
    let mut sides = vec![];
    let mut rect = (length, width);

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
        testing(5, 3, Some(vec![3, 2, 1, 1]));
        testing(3, 5, Some(vec![3, 2, 1, 1]));
        testing(5, 5, None);
        testing(5, 1, Some(vec![1,1,1,1,1]));
    }
}

#![allow(dead_code)]


fn race(v1: i32, v2: i32, g: i32) -> Option<Vec<i32>> {
    if v1 >= v2 { 
        return None;
    }

    let time      = 3600 * g / (v2 - v1);
    let hours     = time / 3600;
    let time_rem  = time % 3600; // Seconds remaining.
    let minutes   = time_rem / 60;
    let seconds  = time_rem % 60;

    Some(vec![hours, minutes, seconds])
}

#[cfg(test)]
mod tests { 
    #[test]
    fn test() {
        assert_eq!(super::race(720, 850, 70), Some(vec![0, 32, 18]));
        assert_eq!(super::race(80, 100, 40), Some(vec![2, 0, 0]));
        assert_eq!(super::race(80, 91, 37), Some(vec![3, 21, 49]));
        assert_eq!(super::race(820, 81, 550), None);
    }
}
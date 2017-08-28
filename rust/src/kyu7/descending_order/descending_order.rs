#![allow(dead_code)]
fn digits_base(base : u64, x: u64) -> Vec<u64> {
    let mut digits = vec![];
    let mut num = x;
    while num != 0 {
        let remainder = num % base;
        num -= remainder;
        num /= base;
        digits.push(remainder);
    }

    digits.reverse();
    digits
}

#[inline]
fn digits_base10(x: u64) -> Vec<u64> {
    digits_base(10, x)
}

fn from_digits(base: u64, digits: &Vec<u64>) -> u64 {
    let mut num = 0;
    let mut base_sq = 1; 
    for digit in digits {
        num     += base_sq * digit;
        base_sq *= base;
    }

    num
}

#[inline]
fn from_digits_base10(digits: &Vec<u64>) -> u64 {
    from_digits(10, digits)
}

fn descending_order(x: u64) -> u64 {
    let mut digits = digits_base10(x);
    digits.sort();
    from_digits_base10(&digits)
}

#[cfg(test)]
mod tests {
    #[test]
    fn returns_expected() {
        assert_eq!(super::descending_order(0), 0);
        assert_eq!(super::descending_order(1), 1);
        assert_eq!(super::descending_order(15), 51);
        assert_eq!(super::descending_order(1021), 2110);
        assert_eq!(super::descending_order(123456789), 987654321);
        assert_eq!(super::descending_order(145263), 654321);
        assert_eq!(super::descending_order(1254859723), 9875543221);
    }

}

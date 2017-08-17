#![allow(dead_code)]


fn add(args: &[i64]) -> i64 {
    args.iter().enumerate().fold(0, |acc, (i, v)| { acc + (*v)*((i as i64)+1) })
}

#[cfg(test)]
mod tests {
    struct TestCase {
        answer : i64,
        test_case : Vec<i64>,
    }

    struct Test {
        tests : Vec<TestCase>,
    }

    fn tests() -> Test {
        Test {
            tests : vec![
                TestCase { answer: 0,     test_case: vec![] },
                TestCase { answer: 204,   test_case: vec![1,2,3,4,5,6,7,8] },
                TestCase { answer: 0,     test_case: vec![0,0,0,0,0,0,0,0] },
                TestCase { answer: -169,  test_case: vec![8,-96,0,0,0,-65,0,0,45] },
                TestCase { answer: -1283, test_case: vec![52,-58,-13,-96,-50,82,9,-100,-89,50] }
            ]
        }
    }

    fn run_tests(tests: &Test) {
        for test in tests.tests.iter() {
            let result = super::add(&test.test_case);
            assert_eq!(result, test.answer);
        }
    }

    #[test]
    fn test_gradual_summation() {
        run_tests(&tests());
    }

    #[test]
    fn basic_tests() {
        assert_eq!(super::add(&[]), 0);
        assert_eq!(super::add(&[4,-3,-2]), -8);
    }
}

struct MiniStringInterpreter {
    cell: u8,
}

impl MiniStringInterpreter {
    fn new() -> MiniStringInterpreter {
        MiniStringInterpreter {
            cell: 0x00,
        }
    }
}

struct MiniStringProgram {
    program : &str,
}

impl MiniStringProgram {
    /// Verify that `program` is a valid MiniString program.
    fn new(program : &str) -> Option<MiniStringProgram> {
        for command in program.chars() {
            match command {
                '+' | '.' => continue,
                _         => return None,
            }
        }
        
        Some(
            MiniStringProgram {
                program: program
            }
        )
    }
}

fn my_first_interpreter(code: &str) -> String {
    unimplemented!()
}

mod tests {
    #[test]
    fn example_test_cases() {
    // Outputs the uppercase English alphabet
    assert_eq!(my_first_interpreter("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+."), "ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    // Hello World Program - outputs the string "Hello, World!"
    assert_eq!(my_first_interpreter("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++.+++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."), "Hello, World!");
    }
}
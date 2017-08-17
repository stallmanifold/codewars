#![allow(dead_code)]
use std::slice;


#[derive(Copy, Clone)]
enum MiniStringCommand {
    IncrementCell,
    PrintCell,
}

struct Program {
    program : Vec<MiniStringCommand>,
}

impl Program {
    /// Verify that `program` is a valid MiniString program.
    fn new(code : &str) -> Program {
        let mut program = vec![];
        for command in code.chars() {
            match command {
                '+' => program.push(MiniStringCommand::IncrementCell),
                '.' => program.push(MiniStringCommand::PrintCell),
                _   => continue,
            }
        }

        Program { program: program }
    }

    fn len(&self) -> usize {
        self.program.len()
    }

    fn iter(&self) -> ProgramIter {
        ProgramIter {
            inner: self.program.iter()
        }
    }
}

struct ProgramIter<'a> {
    inner: slice::Iter<'a, MiniStringCommand>,
}

impl<'a> Iterator for ProgramIter<'a> {
    type Item = &'a MiniStringCommand;

    fn next(&mut self) -> Option<Self::Item> {
        self.inner.next()
    }
}

struct Interpreter {
    cell: u8,
}

impl Interpreter {
    fn new() -> Interpreter {
        Interpreter {
            cell: 0x00,
        }
    }

    fn run(&mut self, program: &Program) -> String {
        let mut output = String::new();
        for command in program.iter() {
            match *command {
                MiniStringCommand::IncrementCell => { self.cell = self.cell.wrapping_add(1); }
                MiniStringCommand::PrintCell     => output.push(self.cell as char),
            }
        }

        output
    }
}

fn my_first_interpreter(code: &str) -> String {
    let mut interpreter = Interpreter::new();
    let program = Program::new(code);
    interpreter.run(&program)
}

mod tests {
    #[test]
    fn example_test_cases() {
        // Outputs the uppercase English alphabet
        assert_eq!(super::my_first_interpreter("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+.+."), "ABCDEFGHIJKLMNOPQRSTUVWXYZ");
        // Hello World Program - outputs the string "Hello, World!"
        assert_eq!(super::my_first_interpreter("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++.+++++++..+++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++.+++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++."), "Hello, World!");
    }
}

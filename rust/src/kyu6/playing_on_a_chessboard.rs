fn game(n: u64) -> Vec<u64> {
    // your code
}

#[cfg(test)]
mod tests {
    fn testing(n: u64, exp: Vec<u64>) -> () {
        assert_eq!(game(n), exp)
    }

    #[test]
    fn basics_game() {
        testing(204, vec![20808]);
        testing(807, vec![651249, 2]);
        testing(5014, vec![12570098]);
        testing(750001, vec![562501500001, 2]);

    }
}

#![allow(dead_code)]


struct DepreciationRateSchedule {
    month : usize,
    depreciation_rate : f64,
}

impl DepreciationRateSchedule {
    fn new(initial_rate: f64) -> DepreciationRateSchedule {
        DepreciationRateSchedule {
            month : 0,
            depreciation_rate : initial_rate,
        }
    }

    fn next(&mut self) -> (usize, f64) {
        self.month += 1;
        // We don't need to check for whether `month` is zero since the 
        // increment takes care of that.
        if self.month % 2 == 0 {
            self.depreciation_rate += 0.5;
        }

        (self.month, self.depreciation_rate)
    }
}

struct ValueSchedule {
    initial_value : f64,
    current_value : f64,
    rate_schedule : DepreciationRateSchedule,
}

impl ValueSchedule {
    fn new(initial_value : f64, rate_schedule : DepreciationRateSchedule) -> ValueSchedule {
        ValueSchedule {
            initial_value : initial_value,
            current_value : initial_value,
            rate_schedule : rate_schedule,
        }
    }

    fn next(&mut self) -> (usize, f64) {
        let rate = self.rate_schedule.next().1;
        self.current_value -= (rate / 100.0) * self.current_value;

        (self.rate_schedule.month, self.current_value)
    }
}

struct SavingsSchedule {
    month : usize,
    total_saved: f64,
    savings_rate : f64,
}

impl SavingsSchedule {
    fn new(savings_rate : f64) -> SavingsSchedule {
        SavingsSchedule {
            month: 0,
            total_saved: 0.0,
            savings_rate: savings_rate
        }
    }

    fn next(&mut self) -> (usize, f64) {
        self.month += 1;
        self.total_saved += self.savings_rate;

        (self.month, self.total_saved)
    }
}

#[derive(Copy, Clone)]
struct PurchaseEntry {
    month         : usize,
    old_car_price : f64,
    new_car_price : f64,
    total_savings : f64,
}

struct PurchaseSchedule {
    terminated    : bool,
    old_car_sched : ValueSchedule,
    new_car_sched : ValueSchedule,
    savings_sched : SavingsSchedule,
    current_entry : PurchaseEntry,
}

impl PurchaseSchedule {
    fn new(start_price_old : f64, 
           start_price_new: f64, 
           savings_per_month: f64, 
           percent_loss_by_month: f64) -> PurchaseSchedule {
        
        let old_car_rate  = DepreciationRateSchedule::new(percent_loss_by_month);
        let old_car_sched = ValueSchedule::new(start_price_old, old_car_rate);
        let new_car_rate  = DepreciationRateSchedule::new(percent_loss_by_month);
        let new_car_sched = ValueSchedule::new(start_price_new, new_car_rate);
        let savings_sched = SavingsSchedule::new(savings_per_month);

        PurchaseSchedule {
            terminated    : false,
            old_car_sched : old_car_sched,
            new_car_sched : new_car_sched,
            savings_sched : savings_sched,
            current_entry : PurchaseEntry { 
                month : 0, 
                old_car_price : start_price_old, 
                new_car_price : start_price_new, 
                total_savings : 0.0,
            },
        }
    }
}

impl Iterator for PurchaseSchedule {
    type Item = PurchaseEntry;

    fn next(&mut self) -> Option<Self::Item> {
        if self.terminated == true {
            return None;
        }
        
        let current_entry = self.current_entry;
        if current_entry.total_savings + current_entry.old_car_price 
            >= current_entry.new_car_price
        {
            self.terminated = true;
            return Some(current_entry);
        }

        let next_old_car_value  = self.old_car_sched.next();
        let next_month          = next_old_car_value.0;
        let next_old_car_price  = next_old_car_value.1;
        let next_new_car_price  = self.new_car_sched.next().1;
        let next_savings_amount = self.savings_sched.next().1;

        self.current_entry = PurchaseEntry {
            month         : next_month, 
            old_car_price : next_old_car_price, 
            new_car_price : next_new_car_price, 
            total_savings : next_savings_amount,
        };

        Some(current_entry)
    }
}

fn nb_months(old: i32, new: i32, saving: i32, perc: f64) -> (i32, i32) {
    let old_f64    = old    as f64;
    let new_f64    = new    as f64;
    let saving_f64 = saving as f64;
    let schedule   = PurchaseSchedule::new(old_f64, new_f64, saving_f64, perc);
    let entry      = schedule.last().unwrap();
    let month      = entry.month;
    let amount_remaining = entry.total_savings + entry.old_car_price - entry.new_car_price;

    (month as i32, amount_remaining.round() as i32)
}

#[cfg(test)]
mod tests {
    fn testing(old: i32, new: i32, saving: i32, perc: f64, exp: (i32, i32)) -> () {
        assert_eq!(super::nb_months(old, new, saving, perc), exp)
    }

    #[test]
    fn basics_nb_months() {
        testing(2000,  8000,  1000, 1.5,  (6,  766));
        testing(12000, 8000,  1000, 1.5,  (0,  4000));
        testing(8000,  12000, 500,  1.0,  (8,  597));
        testing(18000, 32000, 1500, 1.25, (8,  332));
        testing(7500,  32000, 300,  1.55, (25, 122));
    }
}

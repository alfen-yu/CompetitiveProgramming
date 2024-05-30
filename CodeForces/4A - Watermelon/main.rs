use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let w: i32 = input.trim().parse().expect("Invalid input");

    if can_divide_watermelon(w) {
        println!("YES");
    } else {
        println!("NO");
    }
}

fn can_divide_watermelon(w: i32) -> bool {
    // If the weight is less than 4 or odd, it cannot be divided into two even parts
    if w < 4 || w % 2 != 0 {
        return false;
    }
    true
}

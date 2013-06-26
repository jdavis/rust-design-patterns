/*
 * Abstract Factory Design Pattern
 * http://joshldavis.com/rust-design-patterns/abstract-factory/
 */

/*
 * Core Trait that defines a Phone
 */
trait Phone {
    fn call(&self);
}

/*
 * Core Trait that defines a Tablet
 */
trait Tablet {
    fn play_games(&self);
}

/*
 * Core Trait that defines a Factory
 */
trait Factory {
    fn new_phone<T: Phone>(&self) -> T;
    fn new_tablet<T: Tablet>(&self) -> T;
}


/*
 * Define our Apple products. Normally these structs would contain a lot more
 * data.
 */
struct iPhone;

impl Phone for iPhone {
    fn call(&self) {
        println("Look! I'm calling on an iPhone!");
    }
}

struct iPad;

impl Tablet for iPad {
    fn play_games(&self) {
        println("Just playing some games on my iPad.");
    }
}

/*
 * This would contain all stuff required to make Apple devices.
 */
struct AppleFactory;

impl Factory for AppleFactory {
    fn new_phone<T: Phone>(&self) -> T {
        return iPhone;
    }

    fn new_tablet<T: Tablet>(&self) -> T {
        return iPad;
    }
}

/*
 * Define our Google products. Like with Apple's products, these are
 * simplified.
 */

struct Nexus4;

impl Phone for Nexus4 {
    fn call(&self) {
        println("Look! I'm calling on a Nexus 4!");
    }
}

struct Nexus10;

impl Tablet for Nexus10 {
    fn play_games(&self) {
        println("Just playing some games on my Nexus 10.");
    }
}

/*
 * This would contain all stuff required to make Google devices.
 */
struct GoogleFactory;

impl Factory for GoogleFactory {
    fn new_phone<T: Phone>(&self) -> T {
        return Nexus4;
    }

    fn new_tablet<T: Tablet>(&self) -> T {
        return Nexus10;
    }
}

fn main() {

}

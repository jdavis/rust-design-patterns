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
trait Factory<P: Phone, T: Tablet> {
    fn new_phone(&self) -> P;
    fn new_tablet(&self) -> T;
}


/*
 * Define our Apple products. Normally these structs would contain a lot more
 * data.
 */
struct IPhone;

impl Phone for IPhone {
    fn call(&self) {
        println!("Look! I'm calling on an IPhone!");
    }
}

struct IPad;

impl Tablet for IPad {
    fn play_games(&self) {
        println!("Just playing some games on my IPad.");
    }
}

/*
 * Create AppleFactory and implement it for our Apple devices
 */
struct AppleFactory;

impl Factory<IPhone, IPad> for AppleFactory {
    fn new_phone(&self) -> IPhone {
        return IPhone;
    }

    fn new_tablet(&self) -> IPad {
        return IPad;
    }
}

/*
 * Define our Google products. Like with Apple's products, these are
 * simplified.
 */

struct Nexus4;

impl Phone for Nexus4 {
    fn call(&self) {
        println!("Look! I'm calling on a Nexus 4!");
    }
}

struct Nexus10;

impl Tablet for Nexus10 {
    fn play_games(&self) {
        println!("Just playing some games on my Nexus 10.");
    }
}

/*
 * Create GoogleFactory and implement it for our Google devices
 */
struct GoogleFactory;

impl Factory<Nexus4, Nexus10> for GoogleFactory {
    fn new_phone(&self) -> Nexus4 {
        return Nexus4;
    }

    fn new_tablet(&self) -> Nexus10 {
        return Nexus10;
    }
}


fn main() {
    // Create our two different factories
    let apple = AppleFactory;
    let google = GoogleFactory;

    // Both factories use the same interface, so let's just use them

    // Test out creating phones
    let phone = apple.new_phone();
    phone.call();

    let phone = google.new_phone();
    phone.call();

    // Test out creating tablets
    let tablet = apple.new_tablet();
    tablet.play_games();

    let tablet = google.new_tablet();
    tablet.play_games();
}

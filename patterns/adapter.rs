/*
 * Adapter Design Pattern
 * http://joshldavis.com/rust-design-patterns/adapter/
 */

/*
 * Core Trait that defines a basic Rocket Ship
 */
trait RocketShip {
    fn turn_on(&self);
    fn turn_off(&self);
    fn blast_off(&self);
    fn fly(&self);
}

/*
 * Basic struct for a NASA Ship
 */
struct NASAShip;

/*
 * Implement RocketShip trait to add functionality to NASAShip
 */
impl RocketShip for NASAShip {
    fn turn_on(&self) {
        println!("NASA Ship is turning on.")
    }

    fn turn_off(&self) {
        println!("NASA Ship is turning off.")
    }

    fn blast_off(&self) {
        println!("NASA Ship is blasting off.")
    }

    fn fly(&self) {
        println!("NASA Ship is flying away.")
    }
}

/*
 * Uh oh, here is our problem. It's the amazingly advanced SpaceX ship that our
 * astronaut doesn't know how to pilot.
 */
trait SpaceXShip {
    fn ignition(&self);
    fn on(&self);
    fn off(&self);
    fn launch(&self);
    fn fly(&self);
}

/*
 * Basic struct for a SpaceX Dragon rocket ship
 */
struct SpaceXDragon;

/*
 * Implement the SpaceX trait to add functionality to the Space X Dragon
 */
impl SpaceXShip for SpaceXDragon {
    fn ignition(&self) {
        println!("Turning Dragon's ignition.")
    }

    fn on(&self) {
        println!("Turning on the Dragon.")
    }

    fn off(&self) {
        println!("Turning off the Dragon.")
    }

    fn launch(&self) {
        println!("Launching the Dragon")
    }

    fn fly(&self) {
        println!("The Dragon is flying away.")
    }
}

/*
 * Uh oh, the new SpaceXDragon doesn't implement the RocketShip interface. We
 * need to create an adapter that does.
 */

/*
 * Adapter to adapt anything that implements SpaceXShip to the RocketShip trait
 */
struct SpaceXAdapter {
    ship: SpaceXDragon
}

/*
 * SpaceX Adapter that adds RocketShip traits to any SpaceXShip
 */
impl RocketShip for SpaceXAdapter {
    fn turn_on(&self) {
        self.ship.ignition();
        self.ship.on();
    }

    fn turn_off(&self) {
        self.ship.off();
    }

    fn blast_off(&self) {
        self.ship.launch();
    }

    fn fly(&self) {
        self.ship.fly();
    }
}

/*
 * Basic function to pilot ships that implement the RocketShip trait
 */
fn pilot<S: RocketShip>(ship: &S) {
    ship.turn_on();
    ship.blast_off();
    ship.fly();
    ship.turn_off();
    print!("\n");
}

fn main() {
    // Create a new NASAShip
    let saturn5 = NASAShip;

    // Let's fly our NASAShip
    println!("Piloting the Saturn 5.");
    pilot(&saturn5);

    // Create a Dragon
    let dragon = SpaceXDragon;

    // Uh oh, our pilot function doesn't recognize this ship...
    // pilot(&dragon); <-- Gives a compile time error.

    // Let's Adapt our SpaceXDragon ship
    let dragon_adapter = SpaceXAdapter {
        ship: dragon
    };

    // Now we can pilot the Dragon!
    println!("Piloting the Dragon Adapter.");
    pilot(&dragon_adapter);
}

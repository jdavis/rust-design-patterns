/*
 * Adapter Design Pattern
 * http://joshldavis.com/design-patterns/adapter/
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
        println("NASA Ship is turning on.")
    }

    fn turn_off(&self) {
        println("NASA Ship is turning off.")
    }

    fn blast_off(&self) {
        println("NASA Ship is blasting off.")
    }

    fn fly(&self) {
        println("NASA Ship is flying away.")
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

struct SpaceXDragon;

impl SpaceXShip for SpaceXDragon {
    fn ignition(&self) {
        println("Turning Dragon's ignition.")
    }

    fn on(&self) {
        println("Turning on the Dragon.")
    }

    fn off(&self) {
        println("Turing off the Dragon.")
    }

    fn launch(&self) {
        println("Launching the Dragon")
    }

    fn fly(&self) {
        println("The Dragon is flying away.")
    }
}

struct SpaceXAdapter {
    ship: SpaceXDragon
}

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

fn pilot<S: RocketShip>(ship: &S) {
    ship.turn_on();
    ship.blast_off();
    ship.fly();
    ship.turn_off();
    print("\n");
}

fn main() {
    let saturn5 = NASAShip;

    // Let's fly our NASAShip
    println("Piloting the Saturn 5.");
    pilot(&saturn5);

    let dragon = SpaceXDragon;

    // Uh oh, our pilot function doesn't recognize this ship...
    // println("Piloting the Dragon.");
    // pilot(&dragon); <-- Gives a compile time error.

    // Let's Adapt our SpaceXDragon ship
    let dragon_adapter = SpaceXAdapter {
        ship: dragon
    };

    // Now we can pilot the Dragon!
    println("Piloting the Dragon Adapter.");
    pilot(&dragon_adapter);
}

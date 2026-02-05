## Drive System / Electrical Documentation

## Overview

The drives interface takes over from the user-operated paddle switch for vehicle control. In order to preserve user operation modes, the drive system switches it's command inputs between the human and the electronic interface.

## Electrical Infrastructure

The auxiliary electrical infrastructure of the vehicle is provided by a single voltage stepdown module. This module takes the 12V nominal bus of the scooter, tapped from the ignition/key circuit, and provides 5V power to the steering servomotor, Raspberry Pi, both drive DACs, and the drive relays.

Using a monitored/digital step-down in this role enabled amperage monitoring, and power draw estimations. In further exploration of this technology, this implementation or similar would be advised. Technically, at 5V, the steering motor is under-volted, but undervolting in this case was found to not have significant performance degradation.

## Drive Interface

The drive interface primarily consists of two ADCs, and two relays.

The relays, in their nominally closed position, allow passthrough or "connection" of the drive signal from the thumb-throttle potentiometer. When opened, the relays connect to driven outputs of the digital-to-analog converters, and send voltage outputs along those rails.

The potentiometer used by the driver is a wiper-style, with a single input, and two outputs. At zero command, both outputs are driven to about 2.5V. When given an input, one output is pulled high, and the other is driven low. In function, the DACs follow this same logic, one pulls higher, the other pulls lower. 

In addition, the motor controller has several safety features that make this problematic. Primarily, the controller monitors for voltage discontinuities, and input coherence. As such, changeover/switchover events from the manual control to the automatic control must occur at zero throttle command. To the controller, the 2.5V from the potentiometer must seamlessly become the 2.5V from the DACs, or a fault will trigger. This same rule applies in the reverse transition state, switching from automated to manual control requires the output to be zeroed. Additionally, the inputs to the controller are monitored in the time domain, so large instantaneous jumps in throttle from the DAC have the potential to trigger fault modes.

Fault modes (characterized by a generic 7-beep sequence) cannot be reset without a vehicle restart, and should be avoided at all costs. 

Proper sequencing of a drive input for movement is as follows:
1. User throttle at zero
2. DACs are spun-up to 2.5v or "zero" command, and a delay is recommended here
3. Relays are engaged, switching control to digital system
4. DACs are incrementally stepped up to drive command voltage (one goes up, other goes down)
5. Drive command voltage is sustained for the length of the movement
6. DACs are incrementally stepped down to zero
7. Relays are disenaged, returning control to user

Following this cycle will result in minimal fault engagements upon motion.

## Pitfalls / Known Issues

Common issues discovered with this implementation can be found below:

* Large throttle commands can trigger fault modes, typically above 25% forward throttle command. This is theorized to be a result of the usage of two individually-driven digital-to-analog converters. As commanded throttle increases, the noise floor between the two DAC outputs increases, suspected to trigger the fault condition in the controller. This is exascerbated by sustained operation of the throttle.
* Failure to increment/slowly build commanded throttle can trigger fault modes, due to discontinuity checks within the controller.
* The potentiometer is never fully removed from the circuit, and as such may have an unmodeled role in the fault triggering mechanics.
* Improper sequencing in control logic can trigger faults. Similarly, improper timing of input sequencing can have the same effect

## Current State / Reccomendations

Currently, the drive controller is capable of converting impulse (one off) movement inputs into incremental movements for short durations of time. This model was chosen over a sustained movement option for simplicity on the web-controller side. A sustained motion model is certainly more desireable, but as discussed above, the input system is sequence-dependent, and that was difficult to implement during the time allowed. The code to execute this can be found in scooterController.py

For future implementations, a twin-DAC solution should be moved away from, with instead the use of a 5V inverting op-amp providing direct inversion of one signal, without noise floor effects.
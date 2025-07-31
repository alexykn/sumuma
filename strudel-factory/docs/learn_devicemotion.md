---
source_url: https://strudel.cc/learn/devicemotion/
fetched_date: 2025-07-29T17:16:18.483141
title: Device Motion ð Strudel
description: Strudel is a music live coding environment for the browser, porting the TidalCycles pattern language to JavaScript.
---
 # Device Motion

Devicemotion module allows you to use your mobile deviceâs motion sensors (accelerometer, gyroscope, and orientation sensors) to control musical parameters in real-time. This creates opportunities for expressive, movement-based musical interactions.

## Basic Setup

First, you need to enable device motion sensing:


```

enableMotion()

```


This will prompt the user for permission to access device motion sensors.

## Available Motion Parameters

You can access different types of motion data:

| Motion | Long Names & Aliases | Description |
| --- | --- | --- |
| Acceleration | accelerationX (accX), accelerationY (accY), accelerationZ (accZ) | Measures linear acceleration of the device, excluding gravity. Raw values are normalized from g-force. |
| Gravity | gravityX (gravX), gravityY (gravY), gravityZ (gravZ) | Indicates deviceâs orientation relative to Earthâs gravity. Raw values are normalized from Â±9.81 m/sÂ². |
| Rotation | rotationAlpha (rotA, rotZ), rotationBeta (rotB, rotX), rotationGamma (rotG, rotY) | Measures rotation rate around each axis. Raw values (Â±180Â°/s) are normalized. |
| Orientation | orientationAlpha (oriA, oriZ), orientationBeta (oriB, oriX), orientationGamma (oriG, oriY) | Relative orientation from its starting device position. Normalized from:- Alpha: 0Â° to 360Â°- Beta: -180Â° to 180Â°- Gamma: -90Â° to 90Â° |
| Absolute Orientation | absoluteOrientationAlpha (absOriA, absOriZ), absoluteOrientationBeta (absOriB, absOriX), absoluteOrientationGamma (absOriG, absOriY) | **Not available for iOS** Earth-referenced orientation using magnetometer. Same normalization as Orientation. |

Note:

- All motion values are normalized to a range of 0 to 1.
- Not all devices have the same sensors available
Check [DeviceMotionEvent API](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent) for browser compatibility
- Refer to [Oritentation and motion data explained](https://developer.mozilla.org/en-US/docs/Web/API/Device_orientation_events/Orientation_and_motion_data_explained) for more details

### Orientation vs Absolute Orientation

The key difference between regular orientation and absolute orientation is:

- Regular orientation (`oriX/Y/Z`) measures relative changes in device orientation from its starting position
- Absolute orientation (`absOriX/Y/Z`) measures orientation relative to Earthâs magnetic field and gravity, providing consistent absolute values regardless of starting position

For example, if you rotate your device 90 degrees clockwise and then back:

- Regular orientation will show a change during rotation but return to initial values
- Absolute orientation will show the actual compass heading throughout

This makes absolute orientation particularly useful for creating direction-based musical interactions - for example, performers facing north could play one melody while those facing south play another, creating spatially-aware ensemble performances. Regular orientation, on the other hand, is better suited for detecting relative motion and gestures regardless of which direction the performer is facing.

## Basic Example

Hereâs a simple example that uses device motion to control a synthesizer:


```

enableMotion()
// Create a simple melody
$:n("0 1 3 5")
.scale("C:major")
// Use tilt (gravity) to control filter
.lpf(gravityY.range(200, 2000)) // tilt forward/back for filter cutoff
// Use rotation to control effects
.room(rotZ.range(0, 0.8)) // rotate device for reverb amount
.gain(oriX.range(0.2, 0.8)) // tilt left/right for volume
.sound("sawtooth")

```


## Tips for Using Motion Controls

1. Use `.range(min, max)` to map sensor values to musically useful ranges
2. Consider using `.segment()` to smooth out rapid changes in sensor values

## Debugging

You can use `segment(16).log()` to see the raw values from any motion sensor:


```

$_: accX.segment(16).log(); // logs acceleration values to the console

```


This is helpful when calibrating your ranges and understanding how your device responds to different movements.

Remember that device motion works best on mobile devices and may not be available on all desktop browsers. Always test your motion-controlled pieces on the target device type!

 

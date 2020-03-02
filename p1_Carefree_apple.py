"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"triport_adi","name":"triport_22","typeName":"triport","extraConfig":null,"bufferIndex":0},{"hwid":"drivetrain","name":"dt","typeName":"drivetrain","extraConfig":null,"bufferIndex":1}]}"""
Dt = vex.Drivetrain(motor_right, motor_left, 319. 292.1, vex.DistanceUnits.MM)

dt.drive_for(vex.DirectionType.FWD, 35, vex.DistanceUnits.IN)
dt.stop(vex.BrakeType.BRAKE)
sys.sleep(.5)

dt.drive_for(vex.Directiontype.FWD, 5, vex.DistanceUnits.IN)
st.stop(vex.BrakeType.BRAKE)
sys.sleep(.5)

dt.drive_for(vex.DirectionType.FWD, 20, vex.DistanceUnits.IN)
dt.stop(vex.BrakeType.BRake)
sys.sleep(.5)

dt.turn_for(vex.TurnType.RIGHT, 140, vex.RotationUnits.DEG)
dt.stop(vex.BrakeType.BRAKE)
sys.sleep(.5)

dt.drive_for(vex.DirectionType.FWD, 20, vex.DistanceUnits.IN)
dt.stop(vex.BrakeType.BRAKE)
sys.sleep(.5)

dt.drive_for(vex.TurnType.LEFT, 180, vex.RotationUnits.DEG)
dt.stop(vex.BrakeType.BRAKE)
sys.sleep(.5)

dt.drive_for(vex.DirectionType.FWD, 20, vex.DistanceUnits.IN)
dt.stop(vex.BrakeType.BRAKE)
sys.sleep(.5)

dt.turn_for(vex.TurnType.LEFT, 180, vex.RotationUnits.DEG)
dt.stop(vex.BrakeType.BRAKE)
sys.sleep(.5)
		
dt.drive_for(vex.DirectionType.FWD, 20, vex.DistanceUnits.IN)
dt.stop(vex.BrakeType.BRAKE)
sys.sleep(.5)

dt.turn_for(vex.TurnType.LEFT, 180, vex.RotationUnits.DEG)
dt.stop(vex.BrakeType.BRAKE)
sys.sleep(.5)

dt.drive_for(vex.TurnType.RIGHT, 180, vex.RotationUnits.DEG)
dt.stop(vex.BrakeType.BRAKE)
sys.sleep(.5)

dt.drive_for(vex.DirectType.FWD, 60, vex.DistanceUnits.IN)
dt.stop(vex.BrakeType.BRAKE)
sys.sleep(.5)

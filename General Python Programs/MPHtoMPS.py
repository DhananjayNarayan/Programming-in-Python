print("MPH to MPS Conversion App")

 mph = float(input("\nWhat is the speed in miles per hour: "))
 #Convert to mph to mps. Where 1mph= 0.4474 mps
 mps = mph*0.4474
 mps = round(mps, 2)
 print("Your speed in meters per second is " + str(mps) + ".")

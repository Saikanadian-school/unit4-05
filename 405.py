def calculate(height1 , diameter1):
     return str(3.14159 * diameter * height1 ) 
     
height = input('enter the height: ');
diameter = input('enter the diameter: '); 

print('the volume of the cylinder is: {0}'.format(calculate(height, diameter)))


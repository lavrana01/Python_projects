import sys

expected_output = "botter betty bought a bit of butter But the bit of butter botter betty bought was bitter So botter betty bought a better bit of butter"
 
 

def botter_betty():
 global betty_botter
 betty_botter = "Betty Botter bought a bit of butter But the bit of butter Betty Botter bought was bitter So Betty Botter bought a better bit of butter"
  

 betty_botter = betty_botter.replace('Botter', 'betty')
 betty_botter = betty_botter.replace('Betty', 'botter')


def main(args):
    botter_betty()
    assert betty_botter == expected_output, "Failed"
    print ("Success")
if __name__ == '__main__':
    main(sys.argv)

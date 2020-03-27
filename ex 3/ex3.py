from random import randrange

# chance_cliente = randrange(1,100)

def main():
    gasto      = 0
    rolamento1 = 0
    rolamento2 = 0
    rolamento3 = 0

    i=0
    while i < 1000:
        rolamento1+=1
        rolamento2+=1
        rolamento3+=1
        
        if rolamento1 == 100:
            chance_rolamento1 = randrange(1,100)
            if chance_rolamento1 < 10:
                print("rolamento 1 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75

                gasto += 20 + 100
                i+=20
                
                rolamento1 = 0

        if rolamento1 == 110:
            chance_rolamento1 = randrange(1,100)
            if chance_rolamento1 < 23:
                print("rolamento 1 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 20 + 100
                i+=20
                
                rolamento1 = 0

        if rolamento1 == 120:
            chance_rolamento1 = randrange(1,100)
            if chance_rolamento1 < 48:
                print("rolamento 1 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 20 + 100
                i+=20
                
                rolamento1 = 0

        if rolamento1 == 130:
            chance_rolamento1 = randrange(1,100)
            if chance_rolamento1 < 61:
                print("rolamento 1 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 20 + 100
                i+=20
                
                rolamento1 = 0
        
        if rolamento1 == 140:
            chance_rolamento1 = randrange(1,100)
            if chance_rolamento1 < 70:
                print("rolamento 1 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 20 + 100
                i+=20
                
                rolamento1 = 0
        
        if rolamento1 == 150:
            chance_rolamento1 = randrange(1,100)
            if chance_rolamento1 < 82:
                print("rolamento 1 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 20 + 100
                i+=20
                
                rolamento1 = 0
        
        if rolamento1 == 160:
            chance_rolamento1 = randrange(1,100)
            if chance_rolamento1 < 84:
                print("rolamento 1 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 20 + 100
                i+=20
                
                rolamento1 = 0

        if rolamento1 == 170:
            chance_rolamento1 = randrange(1,100)
            if chance_rolamento1 < 90:
                print("rolamento 1 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 20 + 100
                i+=20
                
                rolamento1 = 0

        if rolamento1 == 180:
            chance_rolamento1 = randrange(1,100)
            if chance_rolamento1 < 95:
                print("rolamento 1 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 20 + 100
                i+=20
                
                rolamento1 = 0

        if rolamento1 == 190:
            chance_rolamento1 = randrange(1,100)
            if chance_rolamento1 < 100:
                print("rolamento 1 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 20 + 100
                i+=20
                
                rolamento1 = 0

    
######################################################################################

        if rolamento2 == 100:
            chance_rolamento2 = randrange(1,100)
            if chance_rolamento2 < 10:
                print("rolamento 2 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 30 + 150
                i+=30
                
                rolamento2 = 0

        if rolamento2 == 110:
            chance_rolamento2 = randrange(1,100)
            if chance_rolamento2 < 23:
                print("rolamento 2 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 30 + 150
                i+=30
                
                rolamento2 = 0

        if rolamento2 == 120:
            chance_rolamento2 = randrange(1,100)
            if chance_rolamento2 < 48:
                print("rolamento 2 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 30 + 150
                i+=30
                
                rolamento2 = 0

        if rolamento2 == 130:
            chance_rolamento2 = randrange(1,100)
            if chance_rolamento2 < 61:
                print("rolamento 2 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 30 + 150
                i+=30
                
                rolamento2 = 0
        
        if rolamento2 == 140:
            chance_rolamento2 = randrange(1,100)
            if chance_rolamento2 < 70:
                print("rolamento 2 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 30 + 150
                i+=30
                
                rolamento2 = 0
        
        if rolamento2 == 150:
            chance_rolamento2 = randrange(1,100)
            if chance_rolamento2 < 82:
                print("rolamento 2 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 30 + 150
                i+=30
                
                rolamento2 = 0
        
        if rolamento2 == 160:
            chance_rolamento2 = randrange(1,100)
            if chance_rolamento2 < 84:
                print("rolamento 2 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 30 + 150
                i+=30
                
                rolamento2 = 0

        if rolamento2 == 170:
            chance_rolamento2 = randrange(1,100)
            if chance_rolamento2 < 90:
                print("rolamento 2 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 30 + 150
                i+=30
                
                rolamento2 = 0

        if rolamento2 == 180:
            chance_rolamento2 = randrange(1,100)
            if chance_rolamento2 < 95:
                print("rolamento 2 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 30 + 150
                i+=30
                
                rolamento2 = 0

        if rolamento2 == 190:
            chance_rolamento2 = randrange(1,100)
            if chance_rolamento2 < 100:
                print("rolamento 2 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 30 + 150
                i+=30
                
                rolamento2 = 0


###############################################################################################################


        if rolamento3 == 100:
            chance_rolamento3 = randrange(1,100)
            if chance_rolamento3 < 10:
                print("rolamento 3 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 40 + 200
                i+=40
                
                rolamento3 = 0

        if rolamento3 == 110:
            chance_rolamento3 = randrange(1,100)
            if chance_rolamento3 < 23:
                print("rolamento 3 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 40 + 200
                i+=40
                
                rolamento3 = 0

        if rolamento3 == 120:
            chance_rolamento3 = randrange(1,100)
            if chance_rolamento3 < 48:
                print("rolamento 3 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 40 + 200
                i+=40
                
                rolamento3 = 0

        if rolamento3 == 130:
            chance_rolamento3 = randrange(1,100)
            if chance_rolamento3 < 61:
                print("rolamento 3 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 40 + 200
                i+=40
                
                rolamento3 = 0
        
        if rolamento3 == 140:
            chance_rolamento3 = randrange(1,100)
            if chance_rolamento3 < 70:
                print("rolamento 3 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 40 + 200
                i+=40
                
                rolamento3 = 0
        
        if rolamento3 == 150:
            chance_rolamento3 = randrange(1,100)
            if chance_rolamento3 < 82:
                print("rolamento 3 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 40 + 200
                i+=40
                
                rolamento3 = 0
        
        if rolamento3 == 160:
            chance_rolamento3 = randrange(1,100)
            if chance_rolamento3 < 84:
                print("rolamento 3 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 40 + 200
                i+=40
                
                rolamento3 = 0

        if rolamento3 == 170:
            chance_rolamento3 = randrange(1,100)
            if chance_rolamento3 < 90:
                print("rolamento 3 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 40 + 200
                i+=40
                
                rolamento3 = 0

        if rolamento3 == 180:
            chance_rolamento3 = randrange(1,100)
            if chance_rolamento3 < 95:
                print("rolamento 3 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 40 + 200
                i+=40
                
                rolamento3 = 0

        if rolamento3 == 190:
            chance_rolamento3 = randrange(1,100)
            if chance_rolamento3 < 100:
                print("rolamento 3 quebrou")
                chance_mecanico = randrange(1,100)

                if chance_mecanico < 60:
                    gasto += 25
                elif chance_mecanico >= 60 and chance_mecanico<90:
                    gasto += 50
                else:
                    gasto +=75
                gasto += 40 + 200
                i+=40
                
                rolamento3 = 0

        i+=1
        
    print("gasto: " +str(gasto))


main()
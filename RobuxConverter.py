from time import sleep
print("""               ,   __, ,
   _.._         )\/(,-' (-' `.__
  /_   `-.      )'_      ` _  (_    _.---._
 // \     `-. ,'   `-.    _\`.  `.,'   ,--.\
// -.\       `        `.  \`.   `/   ,'   ||
|| _ `\_         ___    )  )     \  /,-'  ||
||  `---\      ,'__ \   `,' ,--.  \/---. //
 \\  .---`.   / /  | |      |,-.\ |`-._ //
  `..___.'|   \ |,-| |      |_  )||\___//
    `.____/    \\\O| |      \o)// |____/
         /      `---/        \-'  \
         |        ,'|,--._.--')    \
         \       /   `n     n'\    /
          `.   `<   .::`-,-'::.) ,'    
            `.   \-.____,^.   /,'
              `. ;`.,-V-.-.`v'
                \| \     ` \|\
                 ;  `-^---^-'/
                  `-.______,'""")
print("\nConversor de Robux para BRL & USD (SEM TAXA)")
opção = 0
while opção != 4:
    print("""
    [ 1 ] ROBUX PARA USD E BRL
    [ 2 ] USD PARA ROBUX
    [ 3 ] BRL PARA ROBUX
    [ 4 ] SAIR""")
    opção = int(input("QUAL É A SUA OPÇÃO?  "))
    if opção == 1:
        n1 = float(input("DIGITE O VALOR EM ROBUX:  "))
        r1 = n1 * 0.0125
        r2 = r1 * 5.53
        print("\n \n O VALOR DE {:.2f} ROBUX CONVERTIDO PARA USD É DE US$ {:.2f}. \n TAL VALOR CONVERTIDO PARA BRL É DE R$ {:.2f} . ".format(n1, r1, r2))
    elif opção == 2:
        n12 = float(input("DIGITE O VALOR EM USD:  "))
        r12 = n12 * 80
        print("\n \n O VALOR DE US$ {:.2f} CONVERTIDO PARA ROBUX É DE {:.2f} ROBUX .  ".format(n12, r12))
    elif opção == 3:
        n13 = float(input("DIGITE O VALOR EM BRL:  "))
        r13 = n13 / 5.53
        r23 = r13 * 80
        print("\n \n O VALOR DE R$ {:.2f} CONVERTIDO PARA ROBUX É DE {:.2f} ROBUX .  ".format(n13, r23))
    elif opção == 4:
        print("FINALIZANDO...")
    else:
        print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE")
    print("=-=" * 30)
    sleep(3)
print("FIM DO PROGRAMA. VOLTE SEMPRE. \n >>>By Hmstlol & Gulrila<<<")
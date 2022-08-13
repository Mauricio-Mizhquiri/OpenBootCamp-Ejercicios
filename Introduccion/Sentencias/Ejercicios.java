public class Ejercicios {

    public static void main(String[] args) {
        //Primer ejercicio
        System.out.println("\n\t\tPrimer Ejercicio\n");
        int numeroIf = -3;
        comparaNumero(numeroIf);
        
        //Segundo ejercicio
        System.out.println("\n\t\tSegundo Ejercicio\n");
        bucleWhile();

        //Ejercicio 3
        System.out.println("\n\t\tTercer Ejercicio\n");
        bucleDoWhile();

        //Ejercicio 4
        System.out.println("\n\t\tCuarto Ejercicio\n");
        bucleFor();

        //Ejercicio 5
        System.out.println("\n\t\tQuinto Ejercicio\n");
        bloqueSwitch("VEO");
    }

    //Procedimiento que verifica si un número es positivo o negativo
    public static void comparaNumero(int numeroIf){
        if (numeroIf < 0){
            System.out.println("El numero ingresado es menor a cero");
        }else if (numeroIf > 0){
            System.out.println("El numero ingresado es mayor a cero");
        }else{
            System.out.println("El numero ingresado es cero");
        }
    }

    //Procedimieto que muestra el uso del bucle while
    public static void bucleWhile(){
        int numeroWhile = 0;
        while (numeroWhile < 3){
            numeroWhile++;
            System.out.println("valor de numeroWhile: "+numeroWhile);
        }
    }

    //Procedimiento que muestra el uso del bucle doWhile
    public static void bucleDoWhile(){
        int contador = 3;
        do{
            System.out.println("Valor de contador es: "+contador);
        }while(contador > 3);
    }


    //Procedimiento que muestra el uso del bucle for
    public static void bucleFor(){
        for(int numeroFor = 0; numeroFor <= 3; numeroFor++){
            System.out.println("valor de numeroFor: "+numeroFor);
        }
    }

    //Procedimiento que muestra el uso del switch
    public static void bloqueSwitch(String estacionRecibida){
        String estacion = estacionRecibida;
        switch(estacion){
            case "PRIMAVERA":
                System.out.println("Es primavera\n");
                break;
            case "VERANO":
                System.out.println("Es verano\n");
                break;
            case "OTOÑO":
                System.out.println("Es otoño\n");
                break;
            case "INVIERNO":
                System.out.println("Es invierno\n");
                break;
            default:
                System.out.println("El valor ingresado no es una estación\n");
                break;
        }
    }
}


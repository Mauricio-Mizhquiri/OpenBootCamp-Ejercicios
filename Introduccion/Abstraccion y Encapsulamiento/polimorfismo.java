public class polimorfismo {
    public static void main(String[] args) {
        Coche coche = new Coche();
        coche.diHola();
    }
}

class vehiculo{
    public void diHola(){
        System.out.println("Hola!");
    }
}

class Coche extends vehiculo{
    public void diHola(){
        System.out.println("Hola soy un coche");
    }
}
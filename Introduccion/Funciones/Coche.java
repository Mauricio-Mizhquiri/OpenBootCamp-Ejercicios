public class Coche {
    public int numeroPuertas = 0;
    public static void main(String[] args) {
        Coche miCoche = new Coche();
        miCoche.incrementarNumeroPuertas();
        System.out.println("El numero de puertas que tiene el coche es: "+miCoche.numeroPuertas);
    }
    public void incrementarNumeroPuertas(){
        this.numeroPuertas++;
    }
}

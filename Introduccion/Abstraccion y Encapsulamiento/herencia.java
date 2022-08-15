public class herencia {
    public static void main(String[] args) {
        Moto moto = new Moto();
        moto.setSonido("Brrr moto");
        System.out.println(moto.getSonido());
        

    }
}

abstract class Vehiculo{
    int velocidadMaxima;
    String matricula;
    String sonido;

    public Vehiculo(){
        System.out.println("Estoy en el constructor de la clase Vehiculo");
    }

    abstract public String getSonido();
    abstract public void setSonido(String sonido);
    
}

class Coche extends Vehiculo{
    public String getSonido(){
        return this.sonido;
    };
    public void setSonido(String sonido){
        this.sonido = sonido;
    };
}

class CocheElectico extends Coche{


}

class Moto extends Vehiculo{

    public String getSonido(){
        return "Soy un sonido de moto: "+this.sonido;
    }
    public void setSonido(String sonido){
        this.sonido = sonido;
    }
}
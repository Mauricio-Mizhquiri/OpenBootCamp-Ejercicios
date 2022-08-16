public class Cliente extends Persona {
    
    private int credito;

    public int getCredito() {
        return credito;
    }

    public void setCredito(int credito) {
        this.credito = credito;
    }
    
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        
        cliente.setNombre("Juan Perez");
        
        cliente.setEdad(25);
        cliente.setTelefono("+5937585858");
        cliente.setCredito(5000);
        

        System.out.println("\n\tMostrando datos agregados a Cliente\n");
        System.out.println("Hola mundo");
        System.out.println("Nombe: "+cliente.getNombre());
        
        System.out.println("Edad: "+cliente.getEdad());
        System.out.println("Teléfono: "+cliente.getTelefono());
        System.out.println("Crédito: "+cliente.getCredito());
        System.out.println();
    }


    
    
    
}

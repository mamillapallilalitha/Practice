interface View {
  public void forest();
  public void flowers();
 }

class Plants implements View {
 public void forest() {
 System.out.println("trees in forests are so tall");
 }
 public void flowers() {
 System.out.println("flowers looks beautiful");
 }
 }
 class Forest {
 public static void main (String[] args){
 Plants myPlants = new Plants();
 myPlants.forest();
 myPlants.flowers();
 }
 }
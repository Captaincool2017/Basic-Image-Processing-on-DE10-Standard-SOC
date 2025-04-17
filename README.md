# Simulation on Xilinx Vivado

## Steps to Simulate the Project

1. **Create a New Project in Xilinx Vivado**
   - Open Xilinx Vivado and create a new RTL project.
   - Add the following design files:
     - `read_image.v`
     - `write_image.v`
     - `parameter.v`

2. **Include the Testbench File**
   - Add `tb_simulation.v` to the project as your simulation source.

3. **Run Behavioral Simulation**
   - Open the Simulation tab in Vivado.
   - Run the behavioral simulation.
   - In the Tcl Console, enter the following command:
     ```
     run 6ms
     ```
   - Wait for the simulation to complete.

4. **View the Output Image**
   - Close the simulation window.
   - Navigate to the simulation directory inside your project folder.
   - Open the generated `output.bmp` file to view the processed image.

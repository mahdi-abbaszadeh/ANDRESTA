# ANDRESTA
An Automated NoC-Based Design Flow for Real-Time Streaming Applications.


## DESCRIPTION
A design ﬂow that automates the entire ﬂow of mapping a real-time streaming application onto an NoC-based platform and its implementation on an ﬁeld programmable gate array (FPGA). The design ﬂow expects a) a high-level model of the application, described by synchronous data ﬂow (SDF) graphs b) and its real-time constraints. Consequently, it sets up and solves a DSE problem to ﬁnd the optimal solution while delivering the real-time guarantees. The objective of exploring the design space is to map actors to processors based on the actors’ computation bound and the NoC’s communication bound together using constraint programming (CP). A key feature of our design ﬂow is that it can guarantee real-time throughput constraint on top of a best-effort (BE) NoC without the extra overhead of resource reservation paid in guaranteed-service NoCs.


## INSTALLATION and EXECUTION
- Make sure you have already installed the Quratus Prime tool.
- Make sure you have already installed the MiniZinc and add the installation directory to the PATH environment variable.
- Go to "UserFiles" directory and describe your application and hardware configuration in "application.xml" and "hw_conf.xml" respectively.
- Copy your actor's source code in the "actor_codes" directory.
- Go to the "templateEngine" directory in the main root.
- Open the "main.py" python file and specify the address of "Nios II Command Shell.bat" in the "CommandShellAddress" variable.
- Make sure you have connected the FPGA to your computer correctly.
- Run the "main.py".
It will generate necessary files, and finally, download the application on the FPGA.


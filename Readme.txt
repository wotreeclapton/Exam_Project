Samroiyod Exam Application Version 1.0

Copyright (C) 2019 Steven Walden.
All rights reserved.
See license at end of file

=======
Read Me
=======

Table Of Contents:
------------------
1.1 Exam App Overview
1.2 What Does Exam Do?
1.3 Installation Notes
1.4 License information


1.1 Exam App Overview
--------------------

Exam App can display and manage examinations on a mulitpul choice basis utilizing log in accounts and managing scoreing and statistics.


1.2 What Does Exam App Do?
-------------------------

SyncToy synchronizes the files in folders of your choosing. It does so by copying, 
renaming, and deleting files. 


1.3 Installation Notes
----------------------

Installation:

- Exam App is available as a single self-extracting archive executable which runs 
  all of the required setup components when launched. 
- Exam App supports quiet installation by an Administrator user on the target machine. 
  The steps for this are as follows. Please download the self-extracting archive 
  executable and save locally. Extract files from the archive to a target directory. 
  You'll notice 3 MSI files in the set of extracted files. Each of the 3 MSIs can be run 
  in quiet mode using the MSI command line utility (msiexec.exe). The order in which the 
  MSIs need to be installed is: Synchronization-v2.0-{x64/x86}-ENU.msi.msi, ProviderServices-v2.0-{x64/x86}-ENU.msi, 
  SyncToySetup.msi.

Other Notes:

- SyncToy depends on components of the Microsoft Sync Framework which are included in 
  SyncToy setup in case they are not already installed on the target machine. Installing  
  SyncToy along with the dependent components requires the use of an account with 
  Administrator privileges on the target machine. If the Microsoft Sync Framework components 
  are already installed on the target machine, SyncToy can be installed from a 
  non-administrator user account.
- The SyncToy application will stop working if any of the dependent components are 
  uninstalled, which can be fixed by re-running the full install package on the target machine.
- If SyncToy 2.1 is installed using an account which is different than the one that  was used 
  to install previous versions of SyncToy, then the previous version will not be uninstalled.  
  In this case, it is recommended that users uninstall the previous version using the previously 
  used user account before installing SyncToy 2.1.
- If uninstalling SyncToy 2.1, the same user account must be used which was used for 
  installation.

1.4 License information
----------------------

Copyright (c) 2019 Steven Walden

-Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

-The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

-THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.


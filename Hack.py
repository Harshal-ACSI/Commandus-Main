from Library import run_registry_file
import os
run_registry_file(r"C:\Users\parent\Documents\Registry\DeleteBlocksi.reg")
os.system(r"""Get-AppXPackage *WindowsStore* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"} -ErrorAction SilentlyContinue""")
os.system(r"""Get-AppXPackage *Microsoft.XboxGamingOverlay* -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"} -ErrorAction SilentlyContinue""")
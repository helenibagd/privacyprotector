import subprocess
import os
import logging

class PrivacyProtector:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def disable_telemetry(self):
        self.logger.info("Disabling telemetry...")
        commands = [
            "reg add HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection /v AllowTelemetry /t REG_DWORD /d 0 /f",
            "reg add HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection /v MaxTelemetryAllowed /t REG_DWORD /d 0 /f"
        ]
        for cmd in commands:
            self.run_command(cmd)

    def disable_cortana(self):
        self.logger.info("Disabling Cortana...")
        command = "reg add HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search /v AllowCortana /t REG_DWORD /d 0 /f"
        self.run_command(command)

    def configure_firewall(self):
        self.logger.info("Configuring firewall to block all incoming connections...")
        command = "netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound"
        self.run_command(command)

    def disable_location_tracking(self):
        self.logger.info("Disabling location tracking...")
        command = "reg add HKLM\\SYSTEM\\CurrentControlSet\\Services\\lfsvc\\Service\\Configuration /v Status /t REG_DWORD /d 0 /f"
        self.run_command(command)

    def run_command(self, command):
        try:
            subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.logger.info(f"Successfully executed: {command}")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to execute: {command} with error: {e}")

    def protect_privacy(self):
        self.logger.info("Starting Privacy Protection...")
        self.disable_telemetry()
        self.disable_cortana()
        self.configure_firewall()
        self.disable_location_tracking()
        self.logger.info("Privacy Protection Complete.")

if __name__ == "__main__":
    protector = PrivacyProtector()
    protector.protect_privacy()
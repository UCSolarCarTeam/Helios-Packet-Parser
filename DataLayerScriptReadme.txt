Current hard coded content:
- AuxBMS: Defines an enum that is used as type for prechargeState()
    - Return type for getPrechargeState returns a unsigned char instead of enum.(DISCUSS how could this affect code?)
- MotorFaults: Its variable needs to specifically need to know the motor number. Has a QString implemented method that differs from other data type.
- BatteryFaults: Contains methods that aren't found in the CSV (Could add them in for convience)


Test Concern:
-For AuxBMS:
        bool AuxBmsData::auxMaskedBit(const unsigned char mask, unsigned char bits) const
        {
            return static_cast<bool>(bits & mask);
        }
    - Script doesnt add this method, but rather just  "return static_cast<>(mask & bit);" in the getter method
-Name Difference between Comunication layer populator and data layer. Hopefully the script for generating communication layer will resolve this.
#pragma once

#include <QJsonObject>
#include <QJsonArray>
#include <QObject>

class I_AuxBmsData;
class I_CcsData;
class I_BatteryData;
class I_BatteryFaultsData;
class I_DriverControlsData;
class I_KeyMotorData;
class I_LightsData;
class I_MotorDetailsData;
class I_MotorFaultsData;
class I_MpptData;

class I_JsonMessageBuilder : public QObject
{
    Q_OBJECT
public:
    virtual ~I_JsonMessageBuilder() {}
    virtual QJsonObject buildCcsMessage(const I_CcsData& data) = 0;
    $$PUBLIC_FUNCTIONS$$
};

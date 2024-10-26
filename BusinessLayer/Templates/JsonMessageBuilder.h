#pragma once

#include <QJsonObject>
#include <QElapsedTimer>

#include "I_JsonMessageBuilder.h"

class I_PacketChecksumChecker;

class JsonMessageBuilder : public I_JsonMessageBuilder
{
    Q_OBJECT
public:
    virtual ~JsonMessageBuilder() {}
    JsonMessageBuilder();
    JsonMessageBuilder(const I_PacketChecksumChecker& checksumChecker);
    QJsonObject buildCcsMessage(const I_CcsData& data);
    $$PUBLIC_FUNCTIONS$$
};

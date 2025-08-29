""" get Market
{
  "instrument": {
    "epic": "OPEN",
    "symbol": "OPEN",
    "expiry": "-",
    "name": "Opendoor Technologies Inc",
    "lotSize": 1,
    "type": "SHARES",
    "guaranteedStopAllowed": true,
    "streamingPricesAvailable": true,
    "currency": "USD",
    "marginFactor": 20,
    "marginFactorUnit": "PERCENTAGE",
    "openingHours": {
      "mon": [
        "13:30 - 20:00"
      ],
      "tue": [
        "13:30 - 20:00"
      ],
      "wed": [
        "13:30 - 20:00"
      ],
      "thu": [
        "13:30 - 20:00"
      ],
      "fri": [
        "13:30 - 20:00"
      ],
      "sat": [],
      "sun": [],
      "zone": "UTC"
    },
    "country": "United States of America",
    "overnightFee": {
      "longRate": -0.0234291,
      "shortRate": 0.0012069,
      "swapChargeTimestamp": 1755896400000,
      "swapChargeInterval": 1440
    }
  },
  "dealingRules": {
    "minStepDistance": {
      "unit": "POINTS",
      "value": 0.01
    },
    "minDealSize": {
      "unit": "POINTS",
      "value": 10
    },
    "maxDealSize": {
      "unit": "POINTS",
      "value": 26390
    },
    "minSizeIncrement": {
      "unit": "POINTS",
      "value": 0.1
    },
    "minGuaranteedStopDistance": {
      "unit": "PERCENTAGE",
      "value": 75
    },
    "minStopOrProfitDistance": {
      "unit": "PERCENTAGE",
      "value": 0.1
    },
    "maxStopOrProfitDistance": {
      "unit": "PERCENTAGE",
      "value": 100
    },
    "marketOrderPreference": "AVAILABLE_DEFAULT_ON",
    "trailingStopsPreference": "NOT_AVAILABLE"
  },
  "snapshot": {
    "marketStatus": "TRADEABLE",
    "netChange": 1.7,
    "percentageChange": 40.62,
    "updateTime": "2025-08-22T14:41:02.284",
    "delayTime": 0,
    "bid": 5.02,
    "offer": 5.05,
    "high": 5.06,
    "low": 3.43,
    "decimalPlacesFactor": 2,
    "scalingFactor": 1,
    "marketModes": [
      "REGULAR"
    ]
  }
}
"""

""" Show Orders{
  "workingOrders": [
    {
      "workingOrderData": {
        "dealId": "003d014e-0055-311e-0000-000080540613",
        "direction": "BUY",
        "epic": "OPEN",
        "orderSize": 10,
        "leverage": 20,
        "orderLevel": 4,
        "timeInForce": "GOOD_TILL_CANCELLED",
        "createdDate": "2025-08-22T14:34:21.752",
        "createdDateUTC": "2025-08-22T19:34:21.752",
        "guaranteedStop": false,
        "orderType": "LIMIT",
        "trailingStop": false,
        "currencyCode": "USD"
      },
      "marketData": {
        "instrumentName": "Opendoor Technologies Inc",
        "instrumentId": 17171408098514116,
        "expiry": "-",
        "epic": "OPEN",
        "symbol": "OPEN",
        "instrumentType": "SHARES",
        "marketStatus": "TRADEABLE",
        "lotSize": 1,
        "high": 5.06,
        "low": 3.43,
        "percentageChange": 34.45,
        "netChange": 1.62,
        "bid": 4.8,
        "offer": 4.83,
        "updateTime": "2025-08-22T14:34:31.656",
        "updateTimeUTC": "2025-08-22T19:34:31.656",
        "delayTime": 0,
        "streamingPricesAvailable": true,
        "scalingFactor": 1,
        "marketModes": [
          "REGULAR"
        ]
      }
    },
    {
      "workingOrderData": {
        "dealId": "003d014e-0055-311e-0000-000080540614",
        "direction": "SELL",
        "epic": "OPEN",
        "orderSize": 10,
        "leverage": 20,
        "orderLevel": 5,
        "timeInForce": "GOOD_TILL_CANCELLED",
        "createdDate": "2025-08-22T14:34:21.758",
        "createdDateUTC": "2025-08-22T19:34:21.758",
        "guaranteedStop": false,
        "orderType": "LIMIT",
        "trailingStop": false,
        "currencyCode": "USD"
      },
      "marketData": {
        "instrumentName": "Opendoor Technologies Inc",
        "instrumentId": 17171408098514116,
        "expiry": "-",
        "epic": "OPEN",
        "symbol": "OPEN",
        "instrumentType": "SHARES",
        "marketStatus": "TRADEABLE",
        "lotSize": 1,
        "high": 5.06,
        "low": 3.43,
        "percentageChange": 34.45,
        "netChange": 1.62,
        "bid": 4.8,
        "offer": 4.83,
        "updateTime": "2025-08-22T14:34:31.656",
        "updateTimeUTC": "2025-08-22T19:34:31.656",
        "delayTime": 0,
        "streamingPricesAvailable": true,
        "scalingFactor": 1,
        "marketModes": [
          "REGULAR"
        ]
      }
    }
  ]
} 

with take profit

{
  "workingOrders": [
    {
      "workingOrderData": {
        "dealId": "003d014e-0055-311e-0000-000080540629",
        "direction": "BUY",
        "epic": "OPEN",
        "orderSize": 10,
        "leverage": 20,
        "orderLevel": 5.03,
        "timeInForce": "GOOD_TILL_CANCELLED",
        "createdDate": "2025-08-22T14:43:13.925",
        "createdDateUTC": "2025-08-22T19:43:13.925",
        "guaranteedStop": false,
        "orderType": "LIMIT",
        "profitDistance": 0.01,
        "trailingStop": false,
        "currencyCode": "USD"
      },
      "marketData": {
        "instrumentName": "Opendoor Technologies Inc",
        "instrumentId": 17171408098514116,
        "expiry": "-",
        "epic": "OPEN",
        "symbol": "OPEN",
        "instrumentType": "SHARES",
        "marketStatus": "TRADEABLE",
        "lotSize": 1,
        "high": 5.06,
        "low": 3.43,
        "percentageChange": 40.62,
        "netChange": 1.7,
        "bid": 5.02,
        "offer": 5.05,
        "updateTime": "2025-08-22T14:43:16.060",
        "updateTimeUTC": "2025-08-22T19:43:16.060",
        "delayTime": 0,
        "streamingPricesAvailable": true,
        "scalingFactor": 1,
        "marketModes": [
          "REGULAR"
        ]
      }
    }
  ]
}
"""

"""Buy responses:
{
  "dealReference": "o_ba7459e4-2c4a-42f0-ae5d-b7e916d679ba"
}

{
  "errorCode": "error.invalid.size.minvalue"
}
"""

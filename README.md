# [IReporter](https://bmugenya.github.io/IReporter/UI)
[![Build Status](https://travis-ci.com/bmugenya/IReporter.svg?branch=develope)](https://travis-ci.com/bmugenya/IReporter)
[![Coverage Status](https://coveralls.io/repos/github/bmugenya/IReporter/badge.svg?branch=develope)](https://coveralls.io/github/bmugenya/IReporter?branch=develope)


Corruption is a huge bane to Africa’s development. African countries must develop novel and
localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables
any/every citizen to bring any form of corruption to the notice of appropriate authorities and the
general public. Users can also report on things that needs government intervention



### End points
Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/api/v1/record` |  Create a flag. |
|GET| `api/v1/record` | Get all flags.|
|GET| `api/v1/record/<flag_id>` | Get one flag. |
|PATCH| `api/v1/record/<flag_id>` | Update a single flag. |
|DELETE| `api/v1/record/<flag_id>` | Delete a single redflag. |



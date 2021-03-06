# [IReporter](https://bmugenya.github.io/IReporter/UI)

Corruption is a huge bane to Africa’s development. African countries must develop novel and
localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables
any/every citizen to bring any form of corruption to the notice of appropriate authorities and the
general public. Users can also report on things that needs government intervention

## Code Status

[![Build Status](https://travis-ci.com/bmugenya/IReporter.svg?branch=develope)](https://travis-ci.com/bmugenya/IReporter)
[![Coverage Status](https://coveralls.io/repos/github/bmugenya/IReporter/badge.svg?branch=develop)](https://coveralls.io/github/bmugenya/IReporter?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/0e533517d5d3fe5dfa6f/maintainability)](https://codeclimate.com/github/bmugenya/IReporter/maintainability)




### End points
Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/api/v1/auth/register/admin` |  Create an admin. |
|POST| `/api/v1/auth/register/user` |  Create a user. |
|POST| `/api/v1/auth/login/admin` |  login an admin. |
|POST| `/api/v1/auth/login/user` |  login a user. |
|POST| `/api/v1/red-flag` |  Create a flag. |
|GET| `/api/v1/red-flags` | Get all flags.|
|GET| `/api/v1/red-flag/<flag_id>` | Get one flag. |
|PATCH| `/api/v1/red-flag/<flag_id>/location` | Update a flags location. |
|PATCH| `/api/v1/red-flag/<flag_id>/comment` | Update a flags post. |
|PATCH| `/api/v1/red-flag/<flag_id>/status` | Update a flags status. |
|DELETE| `/api/v1/record/<flag_id>` | Delete a single flag. |



## Installation

Clone the Github repository and use pip to install the dependencies
1. `$ git clone https://github.com/bmugenya/IReporter.git`
2. `$ cd/IReporter`
3. `$ source env/bin/activate`
4. `$ pip install -r requirements.txt`


## License

IReporter is released under the [MIT License](https://github.com/bmugenya/IReporter/blob/develop/LICENSE).

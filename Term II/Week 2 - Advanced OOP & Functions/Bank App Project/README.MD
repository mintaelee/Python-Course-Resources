<h1> Design and implement a class that will be used to represent bank accounts.<h1>

<h4>
We will construct the following basic functionalities.

- accounts are uniquely identified by an **account number** 

- account holders have a **first** and **last** name

- **balances** need to be zero or higher, and should not be directly settable.

- if a withdrawal is attempted that would result in nagative funds, the transaction should be declined.

- each deposit and withdrawal must generate a **confirmation number** composed of:

- We will create a **method** that, given a confirmation number, returns:

    - the account number, transaction code (D, W, etc), datetime (UTC format), date time (in whatever timezone is specified in te argument, but more human readable), the transaction ID

    - the transaction type: `D` for deposit, and `W` for withdrawal, `I` for interest deposit, and `X` for declined (in which case the balance remains unaffected)

    - make it so it is a nicely structured object (so can use dotted notation to access these three attributes)
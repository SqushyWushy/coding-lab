# CS 3354 – Assignment 5: REFACTORING in the Large and DESIGN FOR CHANGE

Written by Hector Gonzalez - Summer 2025 CS 3354 Assignment 5

## Overview

This assignment extends our previous rental system to also support movie **sales**. The goal was to refactor the design to allow new features with little changes to my existing code.

## New Features

- **Sales support:** You can now buy movies, not just rent them. Sales are handled using a `Sale` class that extends a new abstract `Transaction` class, shared with `Rental`.
- **Coupons for sales and rentals:** Decorator pattern was used to apply discounts without modifying the base logic.
  - Rental coupons: Half-off, $1 off rentals > $5, free rental after 10 points
  - Sale coupon: Buy 3, pay for 2
- **Point system:** Rentals and sales earn points. Every 10 points = 1 free rental. Orders with 5+ transactions get $5 off.

## Classes Created

- `Transaction.java` (abstract superclass of `Rental` and `Sale`)
- `TransactionDecorator.java` (abstract wrapper)
- `Sale.java`, `SaleDecorator.java`, `BuyTwoGetOneFreeCoupon.java` (sale logic)

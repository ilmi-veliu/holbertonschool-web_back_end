import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
  this._amount = amount;
  this._currency = currency;
  }

  get amount() {
  return this._amount;
  }

  set amount(value) {
  if (typeof amount !== 'number') {
    throw new TypeError('amount must be a number');
  }
  this._amount = value;
  }

  get currency() {
  return this._currency;
  }

  set currency(value) {
  if (!(value instanceof Currency)) {
    throw new TypeError('currency must be a Currency');
  }
  this._currency = value;
  }

  displayFullPrice() {
  return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
  if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
    throw new TypeError('amount and conversionRate must be numbers');
  }
  return amount * conversionRate;
  }
}

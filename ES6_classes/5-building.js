export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
    this.evacuationWarningMessage();
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(sqft) {
    if (typeof sqft !== 'number') throw new TypeError('Sqft must be a number');
    this._sqft = sqft;
  }

  evacuationWarningMessage() {
    if (this.constructor !== Building) throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}

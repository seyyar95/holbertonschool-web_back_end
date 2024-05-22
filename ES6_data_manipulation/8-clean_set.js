/* eslint-disable */
export default function cleanSet(set, startString) {
  let newStr = '';
  const length = startString.length;

  if (length === 0) {
    return '';
  }

  for (let i = 0; i <= set.size; i++) {
    const str = set.values().next().value;
    set.delete(str);

    if (str.includes(startString)) {
      newStr += str.slice(length);
      if (i <= set.size - 1) {
        newStr += '-';
      }
    }
  }

  return newStr;
}

import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'zeroPad'
})
export class ZeroPadPipe implements PipeTransform {

  transform(value: number | string): string {
    // Convert the input value to a string
    let numStr = value.toString();

    // Pad with leading zeros if necessary
    while (numStr.length < 4) {
      numStr = '0' + numStr;
    }

    // Truncate to 4 digits if necessary
    return `OC${numStr}`;
  }

}

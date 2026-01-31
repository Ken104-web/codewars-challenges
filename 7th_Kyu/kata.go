//convert the input str into an array in this case a (rune) slice
// loop through to get the count case estimate
// loop again to convert the count case
package kata

import (
"unicode"
)

func solve(str string) string {
  // Your code here and happy coding!

  case_array := []rune(str)
  upper, lower := 0, 0
  
  // count cases
  for _, i := range case_array{
    if unicode.IsUpper(i) {
      upper++
    } else if unicode.IsLower(i){
      lower++
    }
  }
  
  // convert what found
  
  for i, m := range case_array{
    if upper > lower {
      case_array[i] = unicode.ToUpper(m)
    } else {
      case_array[i]=unicode.ToLower(m)
    }
  }
  return string(case_array)
}
  


//
//  1.swift
//  220213
//
//  Created by 김재희 on 2022/02/13.
//

import Foundation

func solution(_ n:Int) -> Int {
    let arr = "\(n)".compactMap {$0.hexDigitValue }
    return digit(arr.sorted(by: <)) + digit(arr.sorted(by: >))
}

func digit(_ arr: [Int]) -> Int {
    var result = 0
    for (i, n) in arr.enumerated() {
//        result += Int(truncating: NSDecimalNumber(decimal: pow(10, i))) * n
        result += NSDecimalNumber(decimal: pow(10, i)).intValue * n
    }
    return result
}

//func digits(_ n: Int) -> [Int] {
//    if n >= 10 {
//        let first = digits(n / 10)
//        let last = n % 10
//        return first + [last]
//    } else {
//        return [n]
//    }
//}

print(solution(2613))

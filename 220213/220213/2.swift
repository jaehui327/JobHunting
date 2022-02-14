//
//  2.swift
//  220213
//
//  Created by 김재희 on 2022/02/13.
//

import Foundation

func solution(_ n: Int64) -> Int64 {
    var answer: Int64 = 0
    var po = power(n)
    print(po)
    return answer
}

func power(_ n: Int64) -> Int64 {
    var po = 0
    var sum: Int64 = 0
    while sum <= n {
        po += 1
        sum += Int64(truncating: NSNumber(nonretainedObject: pow(2, po)))
        print(po, sum)
    }
    return Int64(po)
}

//func solution(_ n: Int64) -> Int64 {
//    var arr: [Int64] = []
//    var power = -1
//    var exponent: Decimal = 0
//    for i in 0...n - 1 {
//        if exponent == pow(3, power) {
//
//        } else {
//            power += 1
//            exponent = pow(3, power)
//            arr.append(Int64(truncating: NSNumber(nonretainedObject: pow(3, power))))
//        }
//    }
//    return 0
//}

print(solution(2))

func solution(_ n: Int64) -> Int64 {
    var answer: Int64 = 0
    
    var arr: [Int64] = []
    var power = -1
    var count = 0
    var c = 0
    var index = 0
    
    for i in 0...n - 1 {
        if i < count {
            if index > c - arr.count {
                let m = index - arr.count + 1
                var sum: Int64 = 0
                for i in 0...m {
                    sum += arr[i]
//                    power += 1
                }
                answer += sum
                print("1", arr, power, index, m, "answer = ", answer, count)
            } else {
                answer = arr.last ?? 0
                answer += arr[index]
                index += 1
                print("2", arr, power, index, "answer = ", answer, count)
            }
        } else {
            index = 0
            power += 1
            arr.append(NSDecimalNumber(decimal: pow(3, power)).int64Value)
            answer = arr.last ?? 0
            c = NSDecimalNumber(decimal: pow(2, power)).intValue
            count += c
            print("3", arr, power, "answer = ", answer, count)
        }
        
    }
    return answer
}

print(solution(11))

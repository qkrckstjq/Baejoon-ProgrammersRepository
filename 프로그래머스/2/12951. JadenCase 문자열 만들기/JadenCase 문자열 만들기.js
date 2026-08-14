function solution(s) {
    return s.split(' ').map(i=>i.charAt(0).toUpperCase()+i.substring(1).toLowerCase()).join(' ');
}
import fetch from "node-fetch"

export const headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
  Referer: "https://pc.woozooo.com/mydisk.php",
  "Accept-Language": "zh-CN,zh;q=0.9",
  "content-type": "application/x-www-form-urlencoded"
}

export async function get_text(share_url: string) {
  try {
    return await (await fetch(share_url, { headers: headers })).text()
  } catch {
    return ""
  }
}

function remove_notes(html: string): string {
  /**
   * 删除html界面的注释
   */
  // html注释删除
  html = html.replace(/<!--.+?-->|\s+\/\/\s*.+/i, "")
  // js注释删除
  html = html.replace(/("([^\\\"]*(\\.)?)*")|('([^\\\']*(\\.)?)*')|(\/{2,}.*?(\r|\n|$))|(\/\*(\n|.)*?\*\/)/g, function (word: string) {
    // 去除注释后的文本
    return /^\/{2,}/.test(word) || /^\/\*/.test(word) ? "" : word
  })
  return html
}

export async function is_folder_url(share_url: string): Promise<string> {
  /**
   * 判断是不是文件目录分享
   */
  let base_pat = new RegExp("https?://[a-zA-Z0-9-]*?\\.?lanzou\\w.com/.")
  let user_pat = new RegExp("https?://[a-zA-Z0-9-]*?\\.?lanzou\\w.com/(/s/)?b[a-zA-Z0-9]{7,}/?")
  if (share_url.search(base_pat) < 0) return ""
  else if (share_url.search(user_pat) >= 0) return get_text(share_url)
  // vip路径
  else {
    try {
      const html = await get_text(share_url)
      if (html.search('id="infos"') >= 0) return get_text(share_url)
      else return ""
    } catch {
      return ""
    }
  }
}

// function calc_acw_sc__v2(html_text: string): string{
//     const arg1 = re.search(r"arg1='([0-9A-Z]+)'", html_text)
//     const arg1 = arg1.group(1) if arg1 else ""
//     const acw_sc__v2 = hex_xor(unsbox(arg1), "3000176000856006061501533003690027800375")
//     return acw_sc__v2
//   }

// function unsbox(str_arg):
//     v1 = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6, 11, 39, 18, 20, 8, 14, 21, 32, 26, 2,
//           30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36]
//     v2 = ["" for _ in v1]
//     for idx in range(0, len(str_arg)):
//         v3 = str_arg[idx]
//         for idx2 in range(len(v1)):
//             if v1[idx2] == idx + 1:
//                 v2[idx2] = v3

//     res = ''.join(v2)
//     return res

// function hex_xor(str_arg, args){
//     let res = ''
//     for idx in range(0, min(len(str_arg), len(args)), 2):
//         v1 = int(str_arg[idx:idx + 2], 16)
//         v2 = int(args[idx:idx + 2], 16)
//         v3 = format(v1 ^ v2, 'x')
//         if len(v3) == 1:
//             v3 = '0' + v3
//         res += v3

//     return res
//   }

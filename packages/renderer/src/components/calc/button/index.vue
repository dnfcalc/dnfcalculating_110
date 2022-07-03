<script lang="tsx">
  /**
   * @Author: Kritsu
   * @Date:   2021/11/16 23:07:51
   * @Last Modified by:   Kritsu
   * @Last Modified time: 2021/11/17 18:49:42
   */
  import { defineComponent, renderSlot } from "vue"
  import { RouterLink } from "vue-router"

  export default defineComponent({
    name: "calc-button",
    props: {
      small: {
        type: Boolean,
        default: false
      },
      to: {
        type: String,
        default: null
      },
      class: {
        type: [String],
        default: ""
      },
      icon: {
        type: String
      }
    },
    setup(props, { emit, slots }) {
      return () => {
        const proerpties = {
          to: props.to,
          class: {
            [props.class]: !!props.class,
            "i-button cursor-pointer outline-none text-shadow": true,
            small: props.small,
            [`icon-${props.icon}`]: !!props.icon
          }
        }
        const content = renderSlot(slots, "default")
        return props.to ? <RouterLink {...proerpties}>{content}</RouterLink> : <button {...proerpties}>{content}</button>
      }
    }
  })
</script>

<style lang="scss">
  /**
 * @Author: Kritsu
 * @Date:   2021/11/16 23:09:01
 * @Last Modified by:   Kritsu
 * @Last Modified time: 2021/11/17 18:02:58
 */

  .i-button {
    min-width: 56px;
    height: 24px;
    line-height: 20px;

    // font-size: 12px;
    color: #e9c556;
    background: linear-gradient(#223768, #122438);
    border: 1px solid #755f44;
    border-radius: 2px;
    display: block;
    text-align: center;
    text-decoration: none;
    transition: all 200ms ease-in-out;

    &[class*="icon-"] {
      min-width: 1px;
      width: 28px;
      height: 28px;
      padding: 0;
      border: none !important;
      transition: all 0.2s ease-in-out;
    }

    &:hover {
      color: #fee97d;
      background: linear-gradient(#2d4e9f, #153051);
      //  border: 1px solid #e3c18a;
    }

    &:active {
      color: #e9c556;
      background: linear-gradient(#2d4e9f, #122438);
      border: 1px solid #e3c18a;
    }

    &:disabled {
      color: #696969;
      background: linear-gradient(#353535, #1c1c1c);
      border: 1px solid #414141;
      border-radius: 2px;
    }

    &.small {
      min-width: 60px;
      height: 24px;
      line-height: 24px;
      font-size: 12px;
    }
  }

  .i-href {
    display: block;
    text-decoration: none;
  }
</style>

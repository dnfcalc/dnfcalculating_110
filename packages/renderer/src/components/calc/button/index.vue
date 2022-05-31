<script lang="tsx">
  /**
   * @Author: Kritsu
   * @Date:   2021/11/16 23:07:51
   * @Last Modified by:   Kritsu
   * @Last Modified time: 2021/11/17 18:49:42
   */
  import { defineComponent, useSlots, h, renderSlot } from "vue"
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
      }
    },
    setup(props, { emit, slots }) {
      return () => {
        return h(
          //@ts-ignore
          !!props.to ? RouterLink : "button",
          {
            to: props.to,
            class: {
              [props.class]: !!props.class,
              "i-button cursor-pointer outline-none": true,
              small: props.small
            }
          },
          renderSlot(slots, "default")
        )
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
    height: 20px;
    line-height: 16px;

    // font-size: 12px;
    color: #a89679;
    background: linear-gradient(#12396b, #081f3c);
    border: 1px solid #554a3d;
    border-radius: 2px;
    display: block;
    text-align: center;
    text-decoration: none;
    transition: all 200ms ease-in-out;

    &.icon {
      min-width: 28px;
      width: 28px;
    }

    &:hover {
      color: #d4d4b6;
      background: linear-gradient(#195cab, #0b3260);
      border: 1px solid #867760;
    }

    &:active {
      color: #d4d4b6;
      background: linear-gradient(#195cab, #0b3260);
      border: 1px solid #918168;
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

import * as React from "react"
import { cn } from "../../lib/utils"

const Button = React.forwardRef(({ className, children, ...props }, ref) => (
  <button
    ref={ref}
    className={cn(
      "inline-flex items-center justify-center rounded-full font-semibold px-8 py-3 text-lg bg-gradient-to-r from-accent-pink to-accent-purple text-white shadow-card hover:scale-105 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-accent-pink",
      className
    )}
    {...props}
  >
    {children}
  </button>
))
Button.displayName = "Button"

export { Button } 
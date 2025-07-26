import * as React from "react"
import { cn } from "../../lib/utils"

const Card = React.forwardRef(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "rounded-2xl bg-background-accent/80 shadow-card p-6 backdrop-blur-md border border-white/10",
      className
    )}
    {...props}
  />
))
Card.displayName = "Card"

export { Card } 